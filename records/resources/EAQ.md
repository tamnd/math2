---
records:
    - id: EAQN8XZAD6
      kind: monograph
      title: Introduction to Elliptic Curves and Modular Forms
      creators:
        - name: Neal Koblitz
          role: author
      date: "1984"
      msc:
        - code: 11G05
          from: zbmath_search
        - code: 11-01
          from: zbmath_search
        - code: 11F37
          from: zbmath_search
        - code: 11G40
          from: zbmath_search
        - code: 11D09
          from: zbmath_search
        - code: 11G15
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1984"
          ids:
            doi:
                - 10.1007/978-1-4612-0909-6
                - 10.1007/978-1-4684-0255-1
            zbl: "0553.10019"
            zbl_id: "3880803"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1993"
              ids:
                isbn:
                    - "9781461269427"
                    - "9781461209096"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer US
              date: "1984"
              ids:
                isbn:
                    - "9781468402575"
                    - "9781468402551"
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
          native_id: 10.1007/978-1-4612-0909-6
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0255-1
          level: work
        - source: zbmath_search
          snapshot: blake3:a8e1c9c763cc4a7cf0816f17b1654f8f6ec07d6faeb609dc93b9b617c8b4e7e4
          native_id: "3880803"
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
