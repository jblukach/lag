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
    'https://ipv4.afs1.dev.4n6ir.com',
    'https://ipv4.ape1.dev.4n6ir.com',
    'https://ipv4.apne1.dev.4n6ir.com',
    'https://ipv4.apne2.dev.4n6ir.com',
    'https://ipv4.apne3.dev.4n6ir.com',
    'https://ipv4.aps1.dev.4n6ir.com',
    'https://ipv4.aps2.dev.4n6ir.com',
    'https://ipv4.apse1.dev.4n6ir.com',
    'https://ipv4.apse2.dev.4n6ir.com',
    'https://ipv4.apse3.dev.4n6ir.com',
    'https://ipv4.apse4.dev.4n6ir.com',
    'https://ipv4.apse5.dev.4n6ir.com',
    'https://ipv4.apse7.dev.4n6ir.com',
    'https://ipv4.cac1.dev.4n6ir.com',
    'https://ipv4.caw1.dev.4n6ir.com',
    'https://ipv4.euc1.dev.4n6ir.com',
    'https://ipv4.euc2.dev.4n6ir.com',
    'https://ipv4.eun1.dev.4n6ir.com',
    'https://ipv4.eus1.dev.4n6ir.com',
    'https://ipv4.eus2.dev.4n6ir.com',
    'https://ipv4.euw1.dev.4n6ir.com',
    'https://ipv4.euw2.dev.4n6ir.com',
    'https://ipv4.euw3.dev.4n6ir.com',
    'https://ipv4.ilc1.dev.4n6ir.com',
    'https://ipv4.mec1.dev.4n6ir.com',
    'https://ipv4.mes1.dev.4n6ir.com',
    'https://ipv4.mxc1.dev.4n6ir.com',
    'https://ipv4.sae1.dev.4n6ir.com',
    'https://ipv4.use1.dev.4n6ir.com',
    'https://ipv4.use2.dev.4n6ir.com',
    'https://ipv4.usw1.dev.4n6ir.com',
    'https://ipv4.usw2.dev.4n6ir.com',
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