package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	fmt.Println("Advent of Code 2021: Boomaa23")
	fmt.Println("-----------------------------")
	fmt.Println("Which day should be run?")
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	fmt.Println()
	sel_num, _ := strconv.Atoi(input)
	switch sel_num {
	case 1:
		sonarSweep()
		break
	default:
		fmt.Println("Day", input, "was not found")
		return
	}
}

func sonarSweep() {
	path := "input/day1.txt"
	file, err := os.Open(path)
	scanner := bufio.NewScanner(file)
	handleErr(err, true, "Could not read input file at "+path)

	increases := -1
	last := 0
	nums := []int{}
	for scanner.Scan() {
		num, _ := strconv.Atoi(scanner.Text())
		nums = append(nums, num)
		if num > last {
			increases++
		}
		last = num
	}
	fmt.Println("Part 1:", increases, "increases")

	increases = -1
	last_l3t := 0
	curr_l3t := 0
	for i := 0; i < len(nums)-2; i++ {
		curr_l3t = nums[i] + nums[i+1] + nums[i+2]
		if curr_l3t > last_l3t {
			increases++
		}
		last_l3t = curr_l3t
	}
	fmt.Println("Part 2:", increases, "increases")
}
