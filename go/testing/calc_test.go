// テストコードのファイル名は_test.goで終わるようにする

package calc

import "testing"

// テストコードはTestから始まる名前にする
// go testコマンドで実行される
func TestSum(t *testing.T) {
	if sum(1, 2) != 3 {
		t.Fatal("sum(1,2) should be 3, but doesn't match")
	}
}
