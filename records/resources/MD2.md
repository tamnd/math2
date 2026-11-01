---
records:
    - id: MD2ZBBWFKQ
      kind: monograph
      title: Topological Vector Spaces
      creators:
        - name: H. H. Schaefer
          role: author
        - name: M. P. Wolff
          role: author
      date: "1971"
      msc:
        - code: 46-01
          from: zbmath_search
        - code: 46A03
          from: zbmath_search
        - code: 47A10
          from: zbmath_search
        - code: 46A22
          from: zbmath_search
        - code: 46A20
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1971"
          ids:
            doi:
                - 10.1007/978-1-4612-1468-7
                - 10.1007/978-1-4684-9928-5
            zbl: "0212.14001"
            zbl_id: "3336209"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1999"
              ids:
                isbn:
                    - "9781461271550"
                    - "9781461214687"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1971"
              ids:
                isbn:
                    - "9780387053806"
                    - "9781468499285"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.13 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-1468-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9928-5
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3336209"
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
