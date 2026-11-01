---
records:
    - id: FJY0X617TM
      kind: monograph
      title: Lie Groups, Lie Algebras, and Representations
      creators:
        - name: Brian C. Hall
          role: author
      date: "2003"
      msc:
        - code: 22-01
          from: zbmath_search
        - code: "22E60"
          from: zbmath_search
        - code: 17-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2003"
          ids:
            doi:
                - 10.1007/978-0-387-21554-9
                - 10.1007/978-3-319-13467-3
            zbl: "1026.22001"
            zbl_id: "1976856"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2003"
              ids:
                isbn:
                    - "9781441923134"
                    - "9780387215549"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer International Publishing
              date: "2015"
              ids:
                isbn:
                    - "9783319134666"
                    - "9783319134673"
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
          native_id: 10.1007/978-0-387-21554-9
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-319-13467-3
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "1976856"
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
