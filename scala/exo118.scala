object LeetCode118 {
  
  def pascalTriangle(n: Int): Seq[Seq[Int]] = {
    if (n == 0)
      Seq()
    else if (n==1)
      Seq(Seq(1))
    else {
      val t = pascalTriangle(n-1) 
      val l = t.last
      val e = ((0 +: l), (l :+ 0)).zipped.map( _ + _ ) 
      t :+ e
    }
  }

  def main(args: Array[String]) = {
    println(pascalTriangle(2))
    println(pascalTriangle(5))
  }
}
