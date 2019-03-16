data(iris)
iris = iris

setosa = subset(iris, Species == "setosa")
versicolor = subset(iris, Species == "versicolor")
virginica = subset(iris, Species == "virginica")

sub_iris = iris[,-5]
head(sub_iris)

for(i in 1:4){
  print(mean(sub_iris[,i]))
}