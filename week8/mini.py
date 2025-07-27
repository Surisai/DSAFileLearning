###Minimum Spanning Trees###



##Kruskal's Algorithm

KruskalsMST(G=(V,E)){
    # T=[];  //set of edges that form MST, initially empty
    # sort edges in E by its weight

    # //create a set for each vertex
    for(each vertex v in V) {
        makeSet(v);
    }

    for(each edge e=(u,v) in E){
        # //find reps for endpoints of edge
        ep1=findSet(u);
        ep2=findSet(v);

        # //if different reps then they are not in same set
        if(ep1!=ep2){
            # //union them the set together
            union(ep1,ep2);

            # //add e to the result
            add e to T;
        }
    }
}


# Prim's Algorithm

