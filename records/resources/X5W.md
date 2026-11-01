---
records:
    - id: X5WPZPKPMP
      kind: monograph
      title: A Polynomial Approach to Linear Algebra
      creators:
        - name: Paul A. Fuhrmann
          role: author
      date: "1996"
      msc:
        - code: 15-01
          from: zbmath_search
        - code: 93Dxx
          from: zbmath_search
        - code: 93Axx
          from: zbmath_search
        - code: 47B35
          from: zbmath_search
        - code: 15A03
          from: zbmath_search
        - code: 15A04
          from: zbmath_search
        - code: 15A63
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1996"
          ids:
            doi:
                - 10.1007/978-1-4419-8734-1
                - 10.1007/978-1-4614-0338-8
            zbl: "0852.15001"
            zbl_id: "921465"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1996"
              ids:
                isbn:
                    - "9780387946436"
                    - "9781441987341"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2012"
              ids:
                isbn:
                    - "9781461403371"
                    - "9781461403388"
              access:
                class: record
      relations:
        - kind: part_of
          to: W0CC03QJC7
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4419-8734-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4614-0338-8
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "921465"
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
          by: m2 v0.6.13 scope/1
          note: from in to in
---
