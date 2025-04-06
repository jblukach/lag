function measureLatency(url, callback) {
    const startTime = performance.now();
    fetch(url, { method: 'HEAD', cache: 'no-store' })
      .then(() => {
        const endTime = performance.now();
        const latency = endTime - startTime;
        callback(latency);
      })
      .catch(error => {
        callback(null, error);
      });
  }

  const urls = [
    'https://ipv4.afs1.lag.4n6ir.com',
    'https://ipv4.ape1.lag.4n6ir.com',
    'https://ipv4.apne1.lag.4n6ir.com',
    'https://ipv4.apne2.lag.4n6ir.com',
    'https://ipv4.apne3.lag.4n6ir.com',
    'https://ipv4.aps1.lag.4n6ir.com',
    'https://ipv4.aps2.lag.4n6ir.com',
    'https://ipv4.apse1.lag.4n6ir.com',
    'https://ipv4.apse2.lag.4n6ir.com',
    'https://ipv4.apse3.lag.4n6ir.com',
    'https://ipv4.apse4.lag.4n6ir.com',
    'https://ipv4.apse5.lag.4n6ir.com',
    'https://ipv4.apse7.lag.4n6ir.com',
    'https://ipv4.cac1.lag.4n6ir.com',
    'https://ipv4.caw1.lag.4n6ir.com',
    'https://ipv4.euc1.lag.4n6ir.com',
    'https://ipv4.euc2.lag.4n6ir.com',
    'https://ipv4.eun1.lag.4n6ir.com',
    'https://ipv4.eus1.lag.4n6ir.com',
    'https://ipv4.eus2.lag.4n6ir.com',
    'https://ipv4.euw1.lag.4n6ir.com',
    'https://ipv4.euw2.lag.4n6ir.com',
    'https://ipv4.euw3.lag.4n6ir.com',
    'https://ipv4.ilc1.lag.4n6ir.com',
    'https://ipv4.mec1.lag.4n6ir.com',
    'https://ipv4.mes1.lag.4n6ir.com',
    'https://ipv4.mxc1.lag.4n6ir.com',
    'https://ipv4.sae1.lag.4n6ir.com',
    'https://ipv4.use1.lag.4n6ir.com',
    'https://ipv4.use2.lag.4n6ir.com',
    'https://ipv4.usw1.lag.4n6ir.com',
    'https://ipv4.usw2.lag.4n6ir.com',
  ];
  
  function testAllUrls(urls) {
    urls.forEach(url => {
      measureLatency(url, (latency, error) => {
        if (error) {
          console.error(`${url}:`, error);
        } else {
          console.log(`${url}: ${latency.toFixed(2)} ms`);
        }
      });
    });
  }
  
  testAllUrls(urls);