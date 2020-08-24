package main

import (
	"fmt"
	"math"
)

type person struct {
	x              float64
	y              float64
	targetDistance float64
}

func newPerson() *person {
	p := person{}
	p.x = 0
	p.y = 0
	p.targetDistance = 0
	return &p
}

func main() {
	p1, p2 := newPerson(), newPerson()
	var idx int
	fmt.Scan(&idx)
	for i := 0; i < idx; i++ {
		fmt.Scan(&p1.x, &p1.y, &p1.targetDistance, &p2.x, &p2.y, &p2.targetDistance)
		distance := math.Sqrt(math.Pow(p2.x-p1.x, 2) + math.Pow(p2.y-p1.y, 2))
		sum := p2.targetDistance + p1.targetDistance
		sub := math.Abs(p2.targetDistance - p1.targetDistance)

		if distance == 0 {
			if p1.targetDistance == p2.targetDistance {
				fmt.Println("-1")
			} else {
				fmt.Println("0")
			}
		} else if distance == sum || distance == sub {
			fmt.Println("1")
		} else if distance < sum && distance > sub {
			fmt.Println("2")
		} else if distance > sum || distance < sub {
			fmt.Println("0")
		}
	}
}
