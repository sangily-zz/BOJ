fun main() {
    fun sub(a:List<Int>):Int = a[0] - a[1]
    println(sub(readLine()!!.split(" ").map { it.toInt() }))
}
