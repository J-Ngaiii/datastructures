
import java.util.List;

public class Tree {
    protected int val;
    private List<Tree> children;

    public Tree(int val, List<Tree> children) {
        this.val = val;
        this.children = children;
    }

    public Tree(int val) {
        this.val = val;
        this.children = null;
    }

    public Tree(List<Tree> children) {
        this.val = Integer.MIN_VALUE;
        this.children = children;
    }

    public Tree() {
        this.val = Integer.MIN_VALUE;
        this.children = null;
    }

    public int getVal() {
        return val;
    }

    public void setVal(int val) {
        this.val = val;
    }

    public List<Tree> getChildren() {
        return children;
    }

    public void setChildren(List<Tree> children) {
        this.children = children;
    }
}
