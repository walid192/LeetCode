func sortArray(arr []int) []int {
    if len(arr) <= 1 {
		return arr
	}

	middle := len(arr) / 2
	left := sortArray(arr[:middle])
	right := sortArray(arr[middle:])

	return merge(left, right)
    
}


func merge(left, right []int) []int {
	result := make([]int, 0)

	for len(left) > 0 || len(right) > 0 {
		if len(left) == 0 {
			return append(result, right...)
		}
		if len(right) == 0 {
			return append(result, left...)
		}

		if left[0] <= right[0] {
			result = append(result, left[0])
			left = left[1:]
		} else {
			result = append(result, right[0])
			right = right[1:]
		}
	}

	return result
}