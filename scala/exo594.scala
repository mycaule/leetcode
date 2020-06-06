object LeetCode594 {
  
  def longestHarmoniousSub(l: Seq[Int]) = {
    l.zipWithIndex.map({ case (x, i) =>
      l.drop(i).filter(y => Math.abs(y-x) < 2) 
    })
      .filter(x => x.exists(_ != x.head))
      .map(x => (x, x.length)) match {
        case l if l.length > 0 => l.maxBy(_._2)._2 
        case _ => 0
    }
  }

  def main(args: Array[String]) = {
    println(longestHarmoniousSub(Seq(1, 3, 2, 2, 5, 2, 3, 7)))
    println(longestHarmoniousSub(Seq(1, 1, 1, 1, 1)))
    println(longestHarmoniousSub(Seq(1, 2, 1, 3, 0, 0, 2, 2, 1, 3, 3)))
  }
}
