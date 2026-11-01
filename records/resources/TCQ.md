---
records:
    - id: TCQ1JBR84Y
      kind: preprint
      title: 'Asymptotics of Random-Lattice Enumeration: Beyond HKZ via Dense Sublattices'
      creators:
        - name: Thijs Laarhoven
          role: author
      date: "2026-10-11"
      subjects:
        - system: arxiv
          code: cs.CR
        - system: arxiv
          code: math.CO
        - system: arxiv
          code: math.MG
      expressions:
        - key: e1
          kind: version
          label: preprint
          date: "2026-10-11"
          ids:
            arxiv: "2610.15265"
      scope:
        value: border
        rule: border-arxiv
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: arxiv
          snapshot: blake3:e8374453dcab7bada88a6b850ab5bc0a0d87abd798991c12ac2d6c76ecd2c055
          native_id: "2610.15265"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.7 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.7 scope/1
          note: to border
    - id: TCQNMA6N31
      kind: monograph
      title: Hodge Decomposition—A Method for Solving Boundary Value Problems
      creators:
        - name: Günter Schwarz
          role: author
      date: "1995"
      msc:
        - code: 58-02
          from: zbmath_search
        - code: 58A14
          from: zbmath_search
        - code: 58J32
          from: zbmath_search
        - code: 31B20
          from: zbmath_search
        - code: 35F15
          from: zbmath_search
        - code: 35J40
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1995"
          ids:
            doi: 10.1007/bfb0095978
            zbl: "0828.58002"
            zbl_id: "783743"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1995"
              ids:
                isbn:
                    - "9783540600169"
                    - "9783540494034"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0095978
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "783743"
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.14 scope/1
          note: from in to in
---
