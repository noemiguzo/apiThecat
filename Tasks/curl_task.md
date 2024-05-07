# CRUL Task
THE CAT API
## Set api key

export api_key=live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM

## Getting Images

 - curl https://api.thecatapi.com/v1/images/search?api_key=$api_key -v  -H 'authority: api.thecatapi.com' -v

noemi@NGUZMANO-DH01:~/autosetup/ts-test$ curl https://api.thecatapi.com/v1/images/search?api_key=$api_key -v  -H 'authority: api.thecatapi.com' -v
*   Trying 192.178.49.19:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (192.178.49.19) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7ffff6d159c0)
> GET /v1/images/search?api_key= HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
> authority: api.thecatapi.com
>
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 200
< x-dns-prefetch-control: off
< x-frame-options: SAMEORIGIN
< strict-transport-security: max-age=15552000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-xss-protection: 1; mode=block
< vary: Origin
< expires: Tue, 03 Jul 2001 06:00:00 GMT
< last-modified: Wed Mar 06 2024 01:07:02 GMT+0000 (Coordinated Universal Time)
< cache-control: post-check=0, pre-check=0
< authenticated: false
< content-type: application/json; charset=utf-8
< x-response-time: 3ms
< x-cloud-trace-context: 17bc145f8275b81050e3afc5cb12ff3b
< date: Wed, 06 Mar 2024 01:07:02 GMT
< server: Google Frontend
< content-length: 89
<
* Connection #0 to host api.thecatapi.com left intact
[{"id":"4id","url":"https://cdn2.thecatapi.com/images/4id.gif","width":241,"height":300}]noemi@NGUZMANO-DH01:~/autosetup/ts-test$

## GET favoutires

 - curl --location 'https://api.thecatapi.com/v1/favourites' --header 'Content-Type: application/json' --header 'x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM'

noemi@NGUZMANO-DH01:~/autosetup/ts-test$ curl --location 'https://api.thecatapi.com/v1/favourites' --header 'Content-Type: application/json' --header 'x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM' -v
*   Trying 192.178.49.19:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (192.178.49.19) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7fffee8a09c0)
> GET /v1/favourites HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
> content-type: application/json
> x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM
>
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 200
< x-dns-prefetch-control: off
< x-frame-options: SAMEORIGIN
< strict-transport-security: max-age=15552000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-xss-protection: 1; mode=block
< vary: Origin
< retry-after-seconds: 60
< ratelimit-limit: 120
< ratelimit-remaining: 119
< ratelimit-consumed: 1
< ratelimit-reset: 2024-03-06T01:10:58.855Z
< content-type: application/json; charset=utf-8
< x-response-time: 182ms
< x-cloud-trace-context: 501021f985f84129d300b3ba20aaa645
< date: Wed, 06 Mar 2024 01:09:59 GMT
< server: Google Frontend
< content-length: 2
<
* Connection #0 to host api.thecatapi.com left intact
[]

## POST favoutites

 - curl --location 'https://api.thecatapi.com/v1/favourites'  --header 'Content-Type: application/json'  --header 'x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM' --data '{"image_id":"3pc",	"sub_id": "my-user-789"}'

noemi@NGUZMANO-DH01:~/autosetup/ts-test$ curl --location 'https://api.thecatapi.com/v1/favourites'  --header 'Content-Type: application/json'  --header 'x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM' --data '{"image_id":"3pc","sub_id": "my-user-789"}' -v
*   Trying 192.178.49.19:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (192.178.49.19) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7fffbbee89c0)
> POST /v1/favourites HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
> content-type: application/json
> x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM
> content-length: 42
>
* We are completely uploaded and fine
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 200
< x-dns-prefetch-control: off
< x-frame-options: SAMEORIGIN
< strict-transport-security: max-age=15552000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-xss-protection: 1; mode=block
< vary: Origin
< retry-after-seconds: 60
< ratelimit-limit: 120
< ratelimit-remaining: 119
< ratelimit-consumed: 1
< ratelimit-reset: 2024-03-06T01:12:00.625Z
< content-type: application/json; charset=utf-8
< x-response-time: 179ms
< x-cloud-trace-context: 491c0b466eade21ace1e54b8a30099e0
< date: Wed, 06 Mar 2024 01:11:00 GMT
< server: Google Frontend
< content-length: 36
<
* Connection #0 to host api.thecatapi.com left intact
{"message":"SUCCESS","id":232447732}

## DELETE favourites

- curl --location --request DELETE 'https://api.thecatapi.com/v1/favourites/232447732' --header 'Content-Type: application/json' --header 'x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM'

noemi@NGUZMANO-DH01:~/autosetup/ts-test$ curl --location --request DELETE 'https://api.thecatapi.com/v1/favourites/232447732' --header 'Content-Type: application/json' --header 'x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM' -v
*   Trying 192.178.49.19:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (192.178.49.19) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7fffccd839c0)
> DELETE /v1/favourites/232447732 HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
> content-type: application/json
> x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM
>
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 200
< x-dns-prefetch-control: off
< x-frame-options: SAMEORIGIN
< strict-transport-security: max-age=15552000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-xss-protection: 1; mode=block
< vary: Origin
< retry-after-seconds: 60
< ratelimit-limit: 120
< ratelimit-remaining: 119
< ratelimit-consumed: 1
< ratelimit-reset: 2024-03-06T01:13:18.744Z
< content-type: application/json; charset=utf-8
< x-response-time: 239ms
< x-cloud-trace-context: daec9e9e3e8ccb1273bb985178ef7360
< date: Wed, 06 Mar 2024 01:12:18 GMT
< server: Google Frontend
< content-length: 21
<
* Connection #0 to host api.thecatapi.com left intact
{"message":"SUCCESS"}

## POST votes

- curl --location 'https://api.thecatapi.com/v1/votes' --header 'Content-Type: application/json' --header 'x-api-key: apikey' --data '{"image_id":"3pc", "sub_id": "891234", "value":1}' -v


noemi@NGUZMANO-DH01:~/autosetup/ts-test$ curl --location 'https://api.thecatapi.com/v1/votes' --header 'Content-Type: application/json' --header 'x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM' --data '{"image_id":"3pc", "sub_id": "891234", "value":1}' -v

*   Trying 192.178.48.243:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (192.178.48.243) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7fffdf0ca9c0)
> POST /v1/votes HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
> content-type: application/json
> x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM
> content-length: 49
>
* We are completely uploaded and fine
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 201
< x-dns-prefetch-control: off
< x-frame-options: SAMEORIGIN
< strict-transport-security: max-age=15552000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-xss-protection: 1; mode=block
< vary: Origin
< retry-after-seconds: 60
< ratelimit-limit: 120
< ratelimit-remaining: 119
< ratelimit-consumed: 1
< ratelimit-reset: 2024-03-06T01:21:28.497Z
< content-type: application/json; charset=utf-8
< x-response-time: 584ms
< x-cloud-trace-context: 506431fd7fb05924db4c8f8696e2b069
< date: Wed, 06 Mar 2024 01:20:29 GMT
< server: Google Frontend
< content-length: 99
<
* Connection #0 to host api.thecatapi.com left intact
{"message":"SUCCESS","id":1165604,"image_id":"3pc","sub_id":"891234","value":1,"country_code":"US"}

## POST votes - edit vote  'Down' Vote with -1

- curl --location 'https://api.thecatapi.com/v1/votes' --header 'Content-Type: application/json' --header 'x-api-key: apikey' --data '{"image_id":"3pc", "sub_id": "891234", "value":-1}' -v

noemi@NGUZMANO-DH01:~/autoPR/ts-test$ curl  'https://api.thecatapi.com/v1/votes' --header 'Content-Type: application/json' --header "x-api-key: $api_key" --data '{"image_id":"3pc", "sub_id": "891234", "value":-1}' -v
*   Trying 142.251.0.121:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (142.251.0.121) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7ffff07a09c0)
> POST /v1/votes HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
> content-type: application/json
> x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM
> content-length: 50
>
* We are completely uploaded and fine
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 201
< x-dns-prefetch-control: off
< x-frame-options: SAMEORIGIN
< strict-transport-security: max-age=15552000; includeSubDomains
< x-download-options: noopen
< x-content-type-options: nosniff
< x-xss-protection: 1; mode=block
< vary: Origin
< retry-after-seconds: 60
< ratelimit-limit: 120
< ratelimit-remaining: 119
< ratelimit-consumed: 1
< ratelimit-reset: 2024-03-06T13:08:09.036Z
< content-type: application/json; charset=utf-8
< x-response-time: 881ms
< x-cloud-trace-context: a5c167209f8d75ac468430cad12e88aa
< date: Wed, 06 Mar 2024 13:07:09 GMT
< server: Google Frontend
< content-length: 100
<
* Connection #0 to host api.thecatapi.com left intact
{"message":"SUCCESS","id":1165693,"image_id":"3pc","sub_id":"891234","value":-1,"country_code":"BO"}

**Negative tests**
## 1. GET votes without API-key

noemi@NGUZMANO-DH01:~/autosetup/ts-test$ curl  "https://api.thecatapi.com/v1/votes?limit=10&order=DESC" -v
*   Trying 192.178.48.243:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (192.178.48.243) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7fffd963d9c0)
> GET /v1/votes?limit=10&order=DESC HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
>
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 401
< content-type: text/plain; charset=utf-8
< x-cloud-trace-context: f661203646aa796f298caafbed3031bf
< date: Wed, 06 Mar 2024 01:15:08 GMT
< server: Google Frontend
< content-length: 78
<
* Connection #0 to host api.thecatapi.com left intact
AUTHENTICATION_ERROR - you need to send your API Key as the 'x-api-key' header

## 2. GET image invalid image_id

noemi@NGUZMANO-DH01:~/autosetup/ts-test$ curl https://api.thecatapi.com/v1/images/3pc_badid?api_key=$api_key -v
*   Trying 192.178.48.243:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (192.178.48.243) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7ffff4e2a9c0)
> GET /v1/images/3pc_badid?api_key=live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
>
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 400
< content-type: text/plain; charset=utf-8
< x-cloud-trace-context: fecb815561652bd8bff9405e76581d45
< date: Wed, 06 Mar 2024 01:17:53 GMT
< server: Google Frontend
< content-length: 60
<
* Connection #0 to host api.thecatapi.com left intact
Couldn't find an image matching the passed 'id' of 3pc_badid

## 3. POST favourites duplicate sub_id

noemi@NGUZMANO-DH01:~/autosetup/ts-test$ curl --location 'https://api.thecatapi.com/v1/favourites'  --header 'Content-Type: application/json'  --header 'x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM' --data '{"image_id":"3pc","sub_id": "my-user-789"}' -v
*   Trying 192.178.48.243:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (192.178.48.243) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7fffda6869c0)
> POST /v1/favourites HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
> content-type: application/json
> x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM
> content-length: 42
>
* We are completely uploaded and fine
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 400
< content-type: text/plain; charset=utf-8
< x-cloud-trace-context: 24579db8815d923cebfd2753526703a7
< date: Wed, 06 Mar 2024 01:24:24 GMT
< server: Google Frontend
< content-length: 75
<
* Connection #0 to host api.thecatapi.com left intact
DUPLICATE_FAVOURITE - favourites are unique for account + image_id + sub_idnoemi@NGUZMANO-DH01:~/autosetup/ts-test$

## 4. DELETE favourites bad id

noemi@NGUZMANO-DH01:~/autosetup/ts-test$ curl --location --request DELETE 'https://api.thecatapi.com/v1/favourites/232447732' --header 'Content-Type: application/json' --header 'x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM' -v
*   Trying 192.178.49.19:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (192.178.49.19) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7fffbd3ec9c0)
> DELETE /v1/favourites/232447732 HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
> content-type: application/json
> x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM
>
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 400
< content-type: text/plain; charset=utf-8
< x-cloud-trace-context: a7242a6463f3eebd71bcdfa837e2a5d6
< date: Wed, 06 Mar 2024 01:26:57 GMT
< server: Google Frontend
< content-length: 15
<
* Connection #0 to host api.thecatapi.com left intact
IVALID_ACCOUNT

## 5. POST favourites no sent image_id [image_id is required]

noemi@NGUZMANO-DH01:~/autosetup/ts-test$ curl --location 'https://api.thecatapi.com/v1/favourites'  --header 'Content-Type: application/json'  --header 'x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM' --data '{"sub_id": "my-user-789"}' -v
*   Trying 192.178.49.19:443...
* TCP_NODELAY set
* Connected to api.thecatapi.com (192.178.49.19) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/certs/ca-certificates.crt
  CApath: /etc/ssl/certs
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN, server accepted to use h2
* Server certificate:
*  subject: CN=api.thecatapi.com
*  start date: Feb  7 10:38:33 2024 GMT
*  expire date: May  7 11:24:42 2024 GMT
*  subjectAltName: host "api.thecatapi.com" matched cert's "api.thecatapi.com"
*  issuer: C=US; O=Google Trust Services LLC; CN=GTS CA 1D4
*  SSL certificate verify ok.
* Using HTTP2, server supports multi-use
* Connection state changed (HTTP/2 confirmed)
* Copying HTTP/2 data in stream buffer to connection buffer after upgrade: len=0
* Using Stream ID: 1 (easy handle 0x7fffe13679c0)
> POST /v1/favourites HTTP/2
> Host: api.thecatapi.com
> user-agent: curl/7.68.0
> accept: */*
> content-type: application/json
> x-api-key: live_q4NhK64bHnooCcxXqBG2mhoRRThymieDah9FNqONycSezH9SC7HvADbBa1CxqTOM
> content-length: 25
>
* We are completely uploaded and fine
* Connection state changed (MAX_CONCURRENT_STREAMS == 100)!
< HTTP/2 400
< content-type: text/plain; charset=utf-8
< x-cloud-trace-context: 831340608e049ff207f11dad89d8abdb
< date: Wed, 06 Mar 2024 01:29:20 GMT
< server: Google Frontend
< content-length: 22
<
* Connection #0 to host api.thecatapi.com left intact
"image_id" is required


**thanks**
