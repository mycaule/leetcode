object LeetCode658 {
  
  def closestElements(l: Seq[Int], k: Int, x: Int) = {
    l.map(u => (u, Math.abs(u-x)))
      .sortWith((a, b) => a._2 < b._2 || (a._2 == b._2 && a._1 < b._1))
      .take(k)
      .map(_._1)
      .sorted
  }

  def main(args: Array[String]) = {
    println(closestElements(Seq(1, 2, 3, 4, 5), 4, 3))
    println(closestElements(Seq(1, 2, 3, 4, 5), 4, -1))
  }
}
