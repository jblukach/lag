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
    'https://ipv6.afs1.dev.4n6ir.com',
    'https://ipv6.ape1.dev.4n6ir.com',
    'https://ipv6.apne1.dev.4n6ir.com',
    'https://ipv6.apne2.dev.4n6ir.com',
    'https://ipv6.apne3.dev.4n6ir.com',
    'https://ipv6.aps1.dev.4n6ir.com',
    'https://ipv6.aps2.dev.4n6ir.com',
    'https://ipv6.apse1.dev.4n6ir.com',
    'https://ipv6.apse2.dev.4n6ir.com',
    'https://ipv6.apse3.dev.4n6ir.com',
    'https://ipv6.apse4.dev.4n6ir.com',
    'https://ipv6.apse5.dev.4n6ir.com',
    'https://ipv6.apse7.dev.4n6ir.com',
    'https://ipv6.cac1.dev.4n6ir.com',
    'https://ipv6.caw1.dev.4n6ir.com',
    'https://ipv6.euc1.dev.4n6ir.com',
    'https://ipv6.euc2.dev.4n6ir.com',
    'https://ipv6.eun1.dev.4n6ir.com',
    'https://ipv6.eus1.dev.4n6ir.com',
    'https://ipv6.eus2.dev.4n6ir.com',
    'https://ipv6.euw1.dev.4n6ir.com',
    'https://ipv6.euw2.dev.4n6ir.com',
    'https://ipv6.euw3.dev.4n6ir.com',
    'https://ipv6.ilc1.dev.4n6ir.com',
    'https://ipv6.mec1.dev.4n6ir.com',
    'https://ipv6.mes1.dev.4n6ir.com',
    'https://ipv6.mxc1.dev.4n6ir.com',
    'https://ipv6.sae1.dev.4n6ir.com',
    'https://ipv6.use1.dev.4n6ir.com',
    'https://ipv6.use2.dev.4n6ir.com',
    'https://ipv6.usw1.dev.4n6ir.com',
    'https://ipv6.usw2.dev.4n6ir.com',
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