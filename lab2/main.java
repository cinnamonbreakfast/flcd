import java.io.*;
import java.util.*;

class Something {
    public static void main(String[] args)
    {
        HashSet<String> hs = new HashSet<String>();

        hs.add("abc")
        hs.add("bac")
        hs.add("abc")

        hs.iterator().forEach(e => System.out.println(e));
    }
}