from aws_cdk import App, Stack
from stack_content import YtConvertorStack

app = App()

stack = Stack(scope=app, id='YtConvertorStack')
YtConvertorStack(stack=stack)

app.synth()
