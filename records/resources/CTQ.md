---
records:
    - id: CTQBZ92HYT
      kind: monograph
      title: Random Fields
      creators:
        - name: Chris Preston
          role: author
      date: "1976"
      expressions:
        - key: e1
          kind: edition
          date: "1976"
          ids:
            doi: 10.1007/bfb0080563
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540078524"
                    - "9783540381938"
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
          native_id: 10.1007/bfb0080563
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: CTQDSD0HAD
      kind: preprint
      title: A Fast and Stable Square-Root-Free Unitary Core-Chasing Algorithm
      creators:
        - name: Mónica Esquivel-Rosado
          role: author
        - name: Jared L. Aurentz
          role: author
        - name: Giovanni Barbarino
          role: author
        - name: María C. Quintana
          role: author
      date: "2026-10-08"
      subjects:
        - system: arxiv
          code: math.NA
        - system: arxiv
          code: cs.NA
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-08"
          ids:
            arxiv: "2610.12228"
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.12228"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
---
