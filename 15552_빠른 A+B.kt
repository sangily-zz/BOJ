import java.io.BufferedReader
import java.io.BufferedWriter
import java.io.InputStreamReader
import java.io.OutputStreamWriter
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))){
    val bw = BufferedWriter(OutputStreamWriter(System.out))
    repeat(this.readLine().toInt()) {
        val token = StringTokenizer(this.readLine())
        val sum = (token.nextToken().toInt() + token.nextToken().toInt()).toString()
        bw.write(sum + "\n")
    }
    kotlin.io.readLine()
    bw.flush()
    bw.close()
}