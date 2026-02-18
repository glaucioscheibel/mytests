package main

import (
	"fmt"
	"math"
)

func main() {
	var primos [1000]bool

    for i := 0; i < 1000; i++ {
        primos[i] = true
    }

	max := int(math.Sqrt(float64(len(primos))))

	for i := 2; i < max + 1; i++ {
		if primos[i] {
			for j := i * i; j < len(primos); j += i {
				primos[j] = false
			}
		}
	}

	for i := 2; i < len(primos); i++ {
		if primos[i] {
			fmt.Print(i)
			fmt.Print(" ")
		}
	}
}
