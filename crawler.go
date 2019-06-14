package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

const url = "http://jwgl1.hznu.edu.cn/CheckCode.aspx"

func main() {
	base := "captcha/unknown/%d.png"
	serial := 1000
	for i := serial; i < serial+1000; i++ {
		resp, _ := http.Get(url)
		src, _ := ioutil.ReadAll(resp.Body)
		dst, _ := os.Create(fmt.Sprintf(base, i))
		_, _ = dst.Write(src)
	}
}
