
curl 转代码 [Convert curl syntax to Python, Node.js, R, PHP, Strest, Go, JSON, Rust](https://curl.trillworks.com/#python)

eg:
```
curl -u user123:pwd123456 -d "topic_sn=DATA_WARNING_WX_RTX&msg_title=title20190320&msg_content=msg20190320&warning_level=0&receiver=123456" http://data.oa.com/msg/topicmsg.html
```
转换后的python代码
```
import requests

data = {
  'topic_sn': 'DATA_WARNING_WX_RTX',
  'msg_title': 'title20190320',
  'msg_content': 'msg20190320',
  'warning_level': '0',
  'receiver': '123456'
}

response = requests.post('http://data.oa.com/msg/topicmsg.html', data=data, auth=('user123', 'pwd123456'))
```

转换后的go代码

```
package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	client := &http.Client{}
	var data = []byte(`{topic_sn=DATA_WARNING_WX_RTX&msg_title=title20190320&msg_content=msg20190320&warning_level=0&receiver=123456}`)
	req, err := http.NewRequest("POST", "http://data.oa.com/msg/topicmsg.html", data)
	if err != nil {
		log.Fatal(err)
	}
	req.SetBasicAuth("user123", "pwd123456")
	resp, err := client.Do(req)
	if err != nil {
		log.Fatal(err)
	}
	bodyText, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("%s\n", bodyText)
}

```
