---
records:
    - id: 6GBKVV25JV
      kind: monograph
      title: Topology I
      creators:
        - name: S. P. Novikov
          role: editor
      date: "1996"
      expressions:
        - key: e1
          kind: edition
          date: "1996"
          ids:
            doi: 10.1007/978-3-662-10579-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1996"
              ids:
                isbn:
                    - "9783642057359"
                    - "9783662105795"
      relations:
        - kind: part_of
          to: XGZPMQ7BSM
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-10579-5
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: 6GBT11XKAF
      kind: preprint
      title: A note on the $p$-adic inhomogeneous Littlewood conjecture
      creators:
        - name: Sam Chow
          role: author
        - name: Owen Jones
          role: author
      date: "2026-10-11"
      subjects:
        - system: arxiv
          code: math.NT
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-11"
          ids:
            arxiv: "2610.15809"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.15809"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
