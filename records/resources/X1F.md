---
records:
    - id: X1F58NVKZK
      kind: monograph
      title: 'Number Theory Noordwijkerhout 1983: Proceedings of the Journées Arithmétiques held at Noordwijkerhout, The Netherlands July 11–15, 1983'
      creators:
        - name: Hendrik Jager
          role: editor
      date: "1984"
      expressions:
        - key: e1
          kind: edition
          date: "1984"
          ids:
            doi: 10.1007/bfb0099436
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1984"
              ids:
                isbn:
                    - "9783540133568"
                    - "9783540389064"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0099436
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: X1FPG0KYBM
      kind: preprint
      title: Adaptive two-points zero-order accelerated methods for stochastic convex optimization problems
      creators:
        - name: Yuriy Dorn
          role: author
        - name: Osman Osmanov
          role: author
        - name: Timofei Loginov
          role: author
        - name: Nazarii Tupitsa
          role: author
        - name: Darina Dvinskikh
          role: author
        - name: Alexander Gasnikov
          role: author
      date: "2026-10-10"
      subjects:
        - system: arxiv
          code: math.OC
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-10"
          ids:
            arxiv: "2610.15202"
      scope:
        value: in
        rule: S2
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.15202"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to in
---
