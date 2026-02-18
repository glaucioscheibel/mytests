package main

import "fmt"

func bubble(v []int) {
	changed := true
	max := len(v) - 1
	for changed {
		changed = false
		for i := 0; i < max; i++ {
			if v[i] > v[i+1] {
				changed = true
				aux := v[i]
				v[i] = v[i+1]
				v[i+1] = aux
			}
		}
		max--
	}
}

func main() {
	var v = []int{1, 10, 2, 9, 8, 3, 7, 4, 6, 5}
	fmt.Println(v)
	bubble(v)
	fmt.Println(v)
}
