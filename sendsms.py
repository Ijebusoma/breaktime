import nexmo

client = nexmo.Client(key='5346c6cc', secret='*********6dd')

client.send_message({
  'from': 'Nexmo',
  'to': '+2347067214869',
  'text': 'A text message from Nessa, sent using the Nexmo SMS API'
})