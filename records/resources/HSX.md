---
records:
    - id: HSXR0G758Y
      kind: monograph
      title: Schéma de Picard Local
      creators:
        - name: Jean-François Boutot
          role: author
      date: "1978"
      expressions:
        - key: e1
          kind: edition
          date: "1978"
          ids:
            doi: 10.1007/bfb0068424
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1978"
              ids:
                isbn:
                    - "9783540086505"
                    - "9783540359364"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0068424
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: HSXWVKPCQV
      kind: preprint
      title: Curvature, diameter and bounded Betti numbers
      creators:
        - name: Zhongmin Shen
          role: author
        - name: Jyh-Yang Wu
          role: author
      date: "2026-10-13"
      subjects:
        - system: arxiv
          code: math.DG
        - system: arxiv
          code: math.AT
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-13"
          ids:
            arxiv: "2610.18530"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.18530"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
