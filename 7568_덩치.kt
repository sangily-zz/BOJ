fun main() {
	val lol = List(readLine()!!.toInt()) { readLine()!!.split(" ") }
	for (i in lol)
		print("${lol.count { i[0] < it[0] && i[1] < it[1] } + 1} ")
}