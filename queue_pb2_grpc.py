# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import queue_pb2 as queue__pb2

GRPC_GENERATED_VERSION = '1.65.5'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in queue_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class QueueServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.StartQueue = channel.unary_unary(
                '/queue.QueueService/StartQueue',
                request_serializer=queue__pb2.StartQueueRequest.SerializeToString,
                response_deserializer=queue__pb2.StartQueueResponse.FromString,
                _registered_method=True)
        self.ConsumeQueue = channel.unary_stream(
                '/queue.QueueService/ConsumeQueue',
                request_serializer=queue__pb2.ConsumeQueueRequest.SerializeToString,
                response_deserializer=queue__pb2.ConsumeQueueResponse.FromString,
                _registered_method=True)
        self.AddMessage = channel.unary_unary(
                '/queue.QueueService/AddMessage',
                request_serializer=queue__pb2.AddMessageRequest.SerializeToString,
                response_deserializer=queue__pb2.AddMessageResponse.FromString,
                _registered_method=True)


class QueueServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def StartQueue(self, request, context):
        """Start the queue with a given name
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConsumeQueue(self, request, context):
        """Consume the queue with a given name (streaming)
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddMessage(self, request, context):
        """Add a message to the queue
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueueServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'StartQueue': grpc.unary_unary_rpc_method_handler(
                    servicer.StartQueue,
                    request_deserializer=queue__pb2.StartQueueRequest.FromString,
                    response_serializer=queue__pb2.StartQueueResponse.SerializeToString,
            ),
            'ConsumeQueue': grpc.unary_stream_rpc_method_handler(
                    servicer.ConsumeQueue,
                    request_deserializer=queue__pb2.ConsumeQueueRequest.FromString,
                    response_serializer=queue__pb2.ConsumeQueueResponse.SerializeToString,
            ),
            'AddMessage': grpc.unary_unary_rpc_method_handler(
                    servicer.AddMessage,
                    request_deserializer=queue__pb2.AddMessageRequest.FromString,
                    response_serializer=queue__pb2.AddMessageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'queue.QueueService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('queue.QueueService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class QueueService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def StartQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/queue.QueueService/StartQueue',
            queue__pb2.StartQueueRequest.SerializeToString,
            queue__pb2.StartQueueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ConsumeQueue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/queue.QueueService/ConsumeQueue',
            queue__pb2.ConsumeQueueRequest.SerializeToString,
            queue__pb2.ConsumeQueueResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddMessage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/queue.QueueService/AddMessage',
            queue__pb2.AddMessageRequest.SerializeToString,
            queue__pb2.AddMessageResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)