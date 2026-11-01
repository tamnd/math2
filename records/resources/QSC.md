---
records:
    - id: QSC30DARJZ
      kind: monograph
      title: Differential Analysis on Complex Manifolds
      creators:
        - name: Raymond O. Wells
          role: author
      date: "1980"
      msc:
        - code: 32Q99
          from: zbmath_search
        - code: 32-02
          from: zbmath_search
        - code: 58A14
          from: zbmath_search
        - code: "14E25"
          from: zbmath_search
        - code: 58-02
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          label: 2nd edition
          language: en
          date: "1980"
          ids:
            doi:
                - 10.1007/978-0-387-73892-5
                - 10.1007/978-1-4757-3946-6
            zbl: "0435.32004"
            zbl_id: "3678214"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2007-12-06"
              ids:
                isbn:
                    - "9780387738918"
                    - "9780387738925"
              access:
                class: record
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1980"
              ids:
                isbn:
                    - "9781475739480"
                    - "9781475739466"
              access:
                class: record
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-73892-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-3946-6
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "3678214"
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
