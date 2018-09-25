package calc

import "fmt"

// Exampleから始まるテストコードでは標準出力の確認ができる
// （Outputのコメントと標準出力が同じかどうか）
func ExampleHello() {
	fmt.Println("Hello")
	// Output: Hello
}

// 順不同な出力のテスト
func ExampleUnordered() {
	for _, v := range []int{1, 2, 3} {
		fmt.Println(v)
	}
	// Unordered output:
	// 2
	// 3
	// 1
}

// mapのイテレートは順番が不定なのでこのテストは失敗することがある
func ExampleShuffleWillBeFailed() {
	x := map[string]int{"a": 1, "b": 2, "c": 3}
	for k, v := range x {
		fmt.Printf("k=%s v=%d\n", k, v)
	}
	// Output:
	// k=a v=1
	// k=b v=2
	// k=c v=3
}

func ExampleShuffle() {
	x := map[string]int{"a": 1, "b": 2, "c": 3}
	for k, v := range x {
		fmt.Printf("k=%s v=%d\n", k, v)
	}
	// Unordered output:
	// k=a v=1
	// k=b v=2
	// k=c v=3
}
