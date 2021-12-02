package main

import "fmt"

// Handle errors with panic or without
func handleErr(err error, doPanic bool, msg string) {
	if err != nil {
		if doPanic {
			panic(msg)
		} else {
			fmt.Println("ERROR: " + msg)
		}
	}
}
