# -*- coding: utf-8 -*-


class Serializer:

    def __init__(self, string_byte):
        self.string_byte = string_byte

    def put(self, value):
        self.string_byte.append(value+"; ")


class DummyRecord:

    def __init__(self, foo_parameter, bar_parameter):
        # self.serializer=serializer
        self.foo_parameter = foo_parameter
        self.bar_parameter = bar_parameter

    def serialize(self, serializer):
        serializer.put(self.foo_parameter)
        serializer.put(self.bar_parameter)


class OperationExecutionRecord:

    __NO_HOSTNAME__ = "<default-host>"
    __NO_SESSION_ID__ = "<no-session-id>"
    __NO_OPERATION_SIGNATURE__ = "noOperation"
    __NO_TRACE_ID__ = -1
    __NO_TIMESTAMP__ = -1
    __NO_EOI_ESS__ = -1
    __VALUES__ = ["operation_siganture", "session_id",
                  "trace_id", "tin", "tout", "hostname", "eoi", "ess"]

    def __init__(self, operation_signature, session_id,
                 trace_id, tin, tout, hostname, eoi, ess):
        self.operation_signature = (self.__NO_OPERATION_SIGNATURE__
                                    if operation_signature is None
                                    else operation_signature)
        self.session_id = (self.__NO_SESSION_ID__
                           if session_id is None
                           else operation_signature)
        self.trace_id = trace_id
        self.tin = tin
        self.tou = tout
        self.hostname = self.__NO_HOSTNAME__ if hostname is None else hostname
        self.eoi = eoi
        self.ess = ess
        
        def serialize(self,serializer):
            serializer.put(self.operation_signature)
            serializer.put(self.session_id)
            serializer.put(self.tin)
            serializer.put(self.tout)
            serializer.put(self.hostname)
            serializer.put(self.eoi)
            serializer.put(self.ess)
class TraceMetadata:
    __NO_PARENT_TRACEID__ = -1
    __NO_PARENT_ORDER_INDEX__ = -1
    __NO_SESSION_ID__ = "<no-session-id>"
    __NO_HOSTNAME__ = "<default-host>"
    def __init__(self,trace_id, thread_id,
                 session_id, hostname,
                 parent_trace_id,
                 parent_order_id):
        self.trace_id=trace_id
        self.thread_id=thread_id
        self.session_id = (self.__NO_SESSION_ID__
                           if session_id is None
                           else session_id)
        self.hostname = (self.__NO_HOASTNAME__
                           if hostname is None
                           else hostname)
        self.parent_trace_id=parent_trace_id
        self.parent_order_id=parent_order_id
        pass
    def serialize(self,serializer):
        serializer.put(self.trace_id)
        serializer.put(self.thread_id)
        serializer.put(self.session_id)
        serializer.put(self.hostname)
        serializer.put(self.parent_trace_id)
        serializer.put(self.parent_order_id)

class BeforeOperationEvent:
    def __init__(self, timestamp, trace_id, order_index, 
                 operation_signature, class_signature):
        self.timestamp = timestamp
        self.trace_id = trace_id
        self.order_index=order_index
        self.operation_signature=operation_signature
        self.class_signature=class_signature
        pass
    def serialize(self,serializer):
        serializer.put(self.timestamp)
        serializer.put(self.trace_id)
        serializer.put(self.order_index)
        serializer.put(self.operation_signature)
        serializer.put(self.class_signature)

class AfterOperationEvent:
    def __init__(self, timestamp, trace_id, order_index, 
                 operation_signature, class_signature):
        self.timestamp = timestamp
        self.trace_id = trace_id
        self.order_index=order_index
        self.operation_signature=operation_signature
        self.class_signature=class_signature
        
        pass
    def serialize(self,serializer):
        serializer.put(self.timestamp)
        serializer.put(self.trace_id)
        serializer.put(self.order_index)
        serializer.put(self.operation_signature)
        serializer.put(self.class_signature)
        

class AfterOperationFailedEvent:
    def __init__(self, timestamp, trace_id, order_index, 
                 operation_signature, class_signature, exception):
        self.timestamp = timestamp
        self.trace_id = trace_id
        self.order_index=order_index
        self.operation_signature=operation_signature
        self.class_signature=class_signature
        self.exception=exception
        pass
    def serialize(self,serializer):
        serializer.put(self.timestamp)
        serializer.put(self.trace_id)
        serializer.put(self.order_index)
        serializer.put(self.operation_signature)
        serializer.put(self.class_signature)
        serializer.put(self.exception)