import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.*
import java.util.Collections.max

private var N:Int = 0
private var K:Int = 0
private lateinit var W:Array<Int>
private lateinit var V:Array<Int>
private val carried = Stack<Int>()
private val indexStack = Stack<Int>()

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
	N = readLine().toInt()
	K = readLine().toInt()
	W = Array(N) {0}
	V = Array(N) {0}
	for (i in 0 until N) {
		with (StringTokenizer(readLine())) {
			W[i] = nextToken().toInt()
			V[i] = nextToken().toInt()
		}
	}
	val valueSums = Stack<Int>()
	for (i in W.indices) {
		carried.clear()
		carried.push(W[i])
		indexStack.push(i)
		next()
		while (!indexStack.isEmpty())
			valueSums.push(V[indexStack.pop()])
	}
	print(max(valueSums))
}

fun next() {

}