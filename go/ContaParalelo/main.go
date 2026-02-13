package main

import (
	"fmt"
	"strconv"
	"time"
)

func dizAi(id string) {
	for i := 1; i < 21; i++ {
		fmt.Println(id + ": " + strconv.Itoa(i))
	}
}

func main() {
	go dizAi("A")
	go dizAi("B")
	go dizAi("C")
	go dizAi("D")
	time.Sleep(2000 * time.Millisecond)
}
