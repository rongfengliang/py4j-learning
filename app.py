from py4j.java_gateway import JavaGateway, GatewayParameters

gateway = JavaGateway(gateway_parameters=GatewayParameters(port=11111))

stack = gateway.entry_point.getStack()

stack.push("First %s" % ('item'))

item = stack.pop()

print(item)