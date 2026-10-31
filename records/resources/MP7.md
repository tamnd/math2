---
records:
    - id: MP7GA6MQED
      kind: preprint
      title: BKT transition for $\mathsf{Sine}_\beta$
      creators:
        - name: Theodoros Assiotis
          role: author
      date: "2026-10-09"
      subjects:
        - system: arxiv
          code: math.PR
        - system: arxiv
          code: math-ph
        - system: arxiv
          code: math.MP
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-09"
          ids:
            arxiv: "2610.13484"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.13484"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
    - id: MP7J9P010R
      kind: monograph
      title: 'Rational Number Theory in the 20th Century: From PNT to FLT'
      creators:
        - name: Władysław Narkiewicz
          role: author
      date: "2012"
      expressions:
        - key: e1
          kind: edition
          date: "2012"
          ids:
            doi: 10.1007/978-0-85729-532-3
          manifestations:
            - key: m1
              kind: print
              publisher: Springer London
              date: "2012"
              ids:
                isbn:
                    - "9780857295316"
                    - "9780857295323"
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-85729-532-3
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
