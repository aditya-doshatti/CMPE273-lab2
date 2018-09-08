"""The Python implementation of the GRPC Calculator server."""

from concurrent import futures
import time
import grpc
import calculator_pb2
import calculator_pb2_grpc

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def add(self, request, context):
        print("Received: " + str(request.value1) + " and " + str(request.value2))
        return calculator_pb2.Sum(sum = request.value1 + request.value2)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            print("Waiting for input from client, on port 50051")
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
