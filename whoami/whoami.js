function handler(event) {
  const response = {
    statusCode: 200,
    statusDescription: 'OK',
    body: event.viewer.ip,
    headers: {
      'content-type': {value: 'text/html'},
    }
  };
  return response;
}