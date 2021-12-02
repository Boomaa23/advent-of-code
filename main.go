package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	dive()
	return
	fmt.Println("Advent of Code 2021: Boomaa23")
	fmt.Println("-----------------------------")
	fmt.Println("Which day should be run?")
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	sel_num, _ := strconv.Atoi(strings.Trim(input, "\n "))
	switch sel_num {
	case 1:
		sonarSweep()
		break
	case 2:
		dive()
		break
	default:
		fmt.Println("Day", sel_num, "was not found")
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

func dive() {
	path := "input/day2.txt"
	file, err := os.Open(path)
	scanner := bufio.NewScanner(file)
	handleErr(err, true, "Could not read input file at "+path)

	horiz_pos := 0
	depth_pt1 := 0
	depth_pt2 := 0
	aim := 0
	for scanner.Scan() {
		words := strings.Fields(scanner.Text())
		num, _ := strconv.Atoi(words[1])

		switch words[0] {
		case "forward":
			horiz_pos += num
			depth_pt2 += aim * num
			break
		case "down":
			depth_pt1 += num
			aim += num
			break
		case "up":
			depth_pt1 -= num
			aim -= num
			break
		}
	}
	fmt.Println("Part 1: x=", horiz_pos, "y=", depth_pt1, "xy=", horiz_pos*depth_pt1)
	fmt.Println("Part 2: x=", horiz_pos, "y=", depth_pt2, "xy=", horiz_pos*depth_pt2)
}
