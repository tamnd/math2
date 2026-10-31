---
records:
    - id: A3C6M5EJ63
      kind: monograph
      title: Mathematical Models in Population Biology and Epidemiology
      creators:
        - name: Fred Brauer
          role: author
        - name: Carlos Castillo-Chavez
          role: author
      date: "2001"
      expressions:
        - key: e1
          kind: edition
          date: "2001"
          ids:
            doi:
                - 10.1007/978-1-4614-1686-9
                - 10.1007/978-1-4757-3516-1
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2012"
              ids:
                isbn:
                    - "9781461416852"
                    - "9781461416869"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9781441931825"
                    - "9781475735161"
      relations:
        - kind: part_of
          to: 7B8JKAVW9F
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4614-1686-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-3516-1
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: A3CMP0TJK2
      kind: preprint
      title: Quillen's finiteness conjecture for the cotangent complex in characteristic two
      creators:
        - name: Timo Schürg
          role: author
      date: "2026-10-02"
      subjects:
        - system: arxiv
          code: math.AC
        - system: arxiv
          code: math.AG
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-02"
          ids:
            arxiv: "2610.03208"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.03208"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
