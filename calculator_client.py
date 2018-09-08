"""The Python implementation of the GRPC Calculator client."""

from __future__ import print_function
import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        value1 = float(input("Enter 1st Number to be added : "))
        value2 = float(input("Enter 2nd Number to be added : "))
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.add(calculator_pb2.Numbers(value1 = value1, value2 = value2))
    print("Sum: " + str(response.sum))
if __name__ == '__main__':
    run()