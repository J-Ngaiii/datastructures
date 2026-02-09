public class BinaryTree extends Tree{
    private BinaryTree left;
    private BinaryTree right;

    public BinaryTree(int val, BinaryTree left, BinaryTree right) {
        super(val);
        this.left = left;
        this.right = right;
    }
    
     public BinaryTree getLeft() {
        return left;
    }

    public BinaryTree getRight() {
        return right;
    }
}
