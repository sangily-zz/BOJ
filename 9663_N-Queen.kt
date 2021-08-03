import java.util.*

private lateinit var arr: IntArray
private var N = 0
private var count = 0

fun main() {
	val sc = Scanner(System.`in`)
	N = sc.nextInt()
	arr = IntArray(N)
	nQueen(0)
	println(count)
}

fun nQueen(depth: Int) {
	if (depth == N) {
		count++
		return
	}
	for (i in 0 until N) {
		arr[depth] = i
		if (possibility(depth)) {
			nQueen(depth + 1)
		}
	}
}

fun possibility(col: Int): Boolean {
	for (i in 0 until col) {
		if (arr[col] == arr[i]) {
			return false
		} else if (Math.abs(col - i) == Math.abs(arr[col] - arr[i])) {
			return false
		}
	}
	return true
}