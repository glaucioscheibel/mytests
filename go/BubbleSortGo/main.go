package main

import "fmt"

func bubble(v []int) {
	changed := true
	last := len(v) - 1
	for changed {
		changed = false
		for i := 0; i < last; i++ {
			if v[i] > v[i+1] {
				changed = true
				aux := v[i]
				v[i] = v[i+1]
				v[i+1] = aux
			}
		}
		last--
	}
}

func main() {
	var v = []int{1, 10, 2, 9, 8, 3, 7, 4, 6, 5}
	fmt.Println(v)
	bubble(v)
	fmt.Println(v)
}
