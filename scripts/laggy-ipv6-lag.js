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
    'https://ipv6.afs1.lag.4n6ir.com',
    'https://ipv6.ape1.lag.4n6ir.com',
    'https://ipv6.apne1.lag.4n6ir.com',
    'https://ipv6.apne2.lag.4n6ir.com',
    'https://ipv6.apne3.lag.4n6ir.com',
    'https://ipv6.aps1.lag.4n6ir.com',
    'https://ipv6.aps2.lag.4n6ir.com',
    'https://ipv6.apse1.lag.4n6ir.com',
    'https://ipv6.apse2.lag.4n6ir.com',
    'https://ipv6.apse3.lag.4n6ir.com',
    'https://ipv6.apse4.lag.4n6ir.com',
    'https://ipv6.apse5.lag.4n6ir.com',
    'https://ipv6.apse7.lag.4n6ir.com',
    'https://ipv6.cac1.lag.4n6ir.com',
    'https://ipv6.caw1.lag.4n6ir.com',
    'https://ipv6.euc1.lag.4n6ir.com',
    'https://ipv6.euc2.lag.4n6ir.com',
    'https://ipv6.eun1.lag.4n6ir.com',
    'https://ipv6.eus1.lag.4n6ir.com',
    'https://ipv6.eus2.lag.4n6ir.com',
    'https://ipv6.euw1.lag.4n6ir.com',
    'https://ipv6.euw2.lag.4n6ir.com',
    'https://ipv6.euw3.lag.4n6ir.com',
    'https://ipv6.ilc1.lag.4n6ir.com',
    'https://ipv6.mec1.lag.4n6ir.com',
    'https://ipv6.mes1.lag.4n6ir.com',
    'https://ipv6.mxc1.lag.4n6ir.com',
    'https://ipv6.sae1.lag.4n6ir.com',
    'https://ipv6.use1.lag.4n6ir.com',
    'https://ipv6.use2.lag.4n6ir.com',
    'https://ipv6.usw1.lag.4n6ir.com',
    'https://ipv6.usw2.lag.4n6ir.com',
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