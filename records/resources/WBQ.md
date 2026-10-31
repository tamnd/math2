---
records:
    - id: WBQQBZ4FCJ
      kind: preprint
      title: Geometric Identification in Predict-Then-Optimize Learning
      creators:
        - name: Jiaxiao Xu
          role: author
        - name: Changhong Mou
          role: author
        - name: Keji Liu
          role: author
        - name: Dinghua Xu
          role: author
        - name: Yeyu Zhang
          role: author
      date: "2026-09-27"
      subjects:
        - system: arxiv
          code: cs.LG
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-09-27"
          ids:
            arxiv: "2609.33472"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2609.33472"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: WBQRBYAM5F
      kind: monograph
      title: Introduction to Algebra
      creators:
        - name: A. I. Kostrikin
          role: author
      date: "1982"
      expressions:
        - key: e1
          kind: edition
          date: "1982"
          ids:
            doi: 10.1007/978-1-4615-7286-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1982"
              ids:
                isbn:
                    - "9780387907116"
                    - "9781461572862"
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4615-7286-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
