package main

import (
	"fmt"
	"math/rand"
)

func qsort(v []int) []int {
	if len(v) < 2 {
		return v
	}
	var menor, igual, maior []int
	pivot := rand.Int() % len(v)
	for i := 0; i<len(v); i++ {
		if v[i] < v[pivot] {
			menor = append(menor, v[i])
		} else if v[i] > v[pivot] {
			maior = append(maior, v[i])
		} else {
			igual = append(igual, v[i])
		}
	}
	menor = append(qsort(menor), igual...)
	return append(menor, qsort(maior)...)
}

func main() {
	var vetor []int
	vetor = append(vetor, 2, 6, 4, 7, 9, 3, 1, 6, 8)
	fmt.Println(vetor)
	vetor = qsort(vetor)
	fmt.Println(vetor)
}
