---
records:
    - id: 1DKYPR91S1
      kind: monograph
      title: The Arithmetic of Elliptic Curves
      creators:
        - name: Joseph H. Silverman
          role: author
      date: "1986"
      msc:
        - code: 11G05
          from: zbmath_search
        - code: 11-01
          from: zbmath_search
        - code: 11G07
          from: zbmath_search
        - code: 11G20
          from: zbmath_search
        - code: 11G40
          from: zbmath_search
        - code: 14H45
          from: zbmath_search
        - code: 14G05
          from: zbmath_search
        - code: 14H25
          from: zbmath_search
        - code: 14-01
          from: zbmath_search
        - code: 14H52
          from: zbmath_search
        - code: 11D25
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1986"
          ids:
            doi:
                - 10.1007/978-0-387-09494-6
                - 10.1007/978-1-4757-1920-8
            zbl: "0585.14026"
            zbl_id: "3937328"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2009"
              ids:
                isbn:
                    - "9780387094939"
                    - "9780387094946"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1986"
              ids:
                isbn:
                    - "9781475719222"
                    - "9781475719208"
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
          native_id: 10.1007/978-0-387-09494-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-1920-8
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3937328"
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
